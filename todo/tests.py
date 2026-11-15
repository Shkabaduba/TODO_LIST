from django.test import TestCase
from django.urls import reverse

from todo.models import Task, Tag


class ModelTest(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="test")
        self.assertEqual(str(tag), "test")

    def test_task_str(self):
        task = Task.objects.create(content="test")
        self.assertEqual(str(task), "test")

    def test_task_ordering(self):
        task_1 = Task.objects.create(content="test", is_done=False)
        task_2 = Task.objects.create(content="test2", is_done=True)
        task_3 = Task.objects.create(content="test3", is_done=False)

        self.assertEqual(
            list(Task.objects.all()),
            [task_3, task_1, task_2],
        )

    def test_toggle_task(self):
        task = Task.objects.create(content="test")
        url = reverse("todo:task-toggle", args=[task.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse("todo:task-list"))
        task.refresh_from_db()
        self.assertTrue(task.is_done)

        self.client.post(url)
        task.refresh_from_db()
        self.assertFalse(task.is_done)


class TaskViewTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="test")
        self.task = Task.objects.create(content="Test task")

    def test_task_list_page(self):
        response = self.client.get(reverse("todo:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test task")

    def test_task_create(self):
        response = self.client.post(
            reverse("todo:task-create"),
            {"content": "New task", "tags": [self.tag.id]},
        )
        self.assertRedirects(response, reverse("todo:task-list"))
        self.assertTrue(Task.objects.filter(content="New task").exists())

    def test_task_update(self):
        response = self.client.post(
            reverse("todo:task-update", args=[self.task.id]),
            {"content": "Updated task"},
        )
        self.assertRedirects(response, reverse("todo:task-list"))
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated task")

    def test_task_delete(self):
        response = self.client.post(
            reverse("todo:task-delete", args=[self.task.id])
        )
        self.assertRedirects(response, reverse("todo:task-list"))
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())


class TagViewTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="test")

    def test_tag_list_page(self):
        response = self.client.get(reverse("todo:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test")

    def test_tag_create(self):
        response = self.client.post(reverse("todo:tag-create"),
                                    {"name": "New tag"},
                                    )
        self.assertRedirects(response, reverse("todo:tag-list"))
        self.assertTrue(Tag.objects.filter(name="New tag").exists())

    def test_tag_update(self):
        response = self.client.post(
            reverse("todo:tag-update", args=[self.tag.id]),
            {"name": "Updated tag"},
        )
        self.assertRedirects(response, reverse("todo:tag-list"))
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "Updated tag")

    def test_tag_delete(self):
        response = self.client.post(
            reverse("todo:tag-delete", args=[self.tag.id])
        )
        self.assertRedirects(response, reverse("todo:tag-list"))
        self.assertFalse(Tag.objects.filter(id=self.tag.id).exists())

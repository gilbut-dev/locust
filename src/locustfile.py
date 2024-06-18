from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def about(self):
        self.client.get("/corp/notices")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)

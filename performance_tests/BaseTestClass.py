from time import time
import requests


class PerformanceTest():
    def __init__(self, url, load_time):
        self.url = url
        self.load_time = load_time
        self.endpoint_responses_time = []

    def load_endpoint(self):
        """ Runs nested function repeatedly for specified period of time in minutes"""
        running_time = 0
        while running_time < self.load_time / 60:
            start = time()
            requests.get(self.url)
            response_time = time() - start
            running_time = running_time + response_time
            self.endpoint_responses_time.append(response_time)

    def count_standard_deviation(self) -> float:
        return round(sum((x - (sum(self.endpoint_responses_time) / len(self.endpoint_responses_time))) ** 2 for x in self.endpoint_responses_time) / (
                    len(self.endpoint_responses_time) - 1) ** 0.5, 2)

    def count_mean_value(self) -> float:
        return round(sum(self.endpoint_responses_time) / len(self.endpoint_responses_time), 2)

    def print_result(self) -> None:
        self.load_endpoint()
        mean = self.count_mean_value()
        standard_deviation = self.count_standard_deviation()
        print(f"{self.url} : mean {mean}, standard_deviation {standard_deviation}")
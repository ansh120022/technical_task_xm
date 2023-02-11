from BaseTestClass import PerformanceTest

base_url = 'http://localhost'

test_people_endpoint = PerformanceTest(url=f'{base_url}/people/10/', load_time=2)
test_people_endpoint.print_result()

test_planets_endpoint = PerformanceTest(url=f'{base_url}/planets/20/', load_time=2)
test_planets_endpoint.print_result()

test_starships_endpoint = PerformanceTest(url=f'{base_url}/starships/30/', load_time=2)
test_starships_endpoint.print_result()


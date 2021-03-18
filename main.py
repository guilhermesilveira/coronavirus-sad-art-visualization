import json

import tweepy

import time


def current_time():
    return round(time.time())


def run(configuration):
    auth = tweepy.OAuthHandler(configuration["api_key"], configuration["api_secret_key"])
    auth.set_access_token(configuration["access_token"], configuration["access_token_secret"])

    api = tweepy.API(auth)

    # limit is 1/36 seconds
    counter = 0
    daily_death_count = 2736
    seconds_between_deaths = (24 * 60 * 60.0) / daily_death_count
    print(f"{round(seconds_between_deaths, 2)} seconds between deaths")

    tweet_rate = max(37, seconds_between_deaths)
    print(f"tweet rate will be every {tweet_rate} seconds, due to API limits")
    starting_time = current_time()
    print(starting_time)
    print(api.update_status(
        "Dificuldade em entender as mortes de covid nas próximas 24 horas? Eu ajudo. #covid19 #brasil #covidvisualization"))

    for counter in range(1, daily_death_count + 1):
        elapsed_seconds = (current_time() - starting_time)
        print(elapsed_seconds)
        t = f"{counter} mortos #covid19 #brasil #covidvisualization"
        print(f"Elapsed {elapsed_seconds} - {t}")
        print(api.update_status(t))
        time.sleep(tweet_rate)


def load_config():
    data = json.load(open('keys.json'))
    return data


if __name__ == '__main__':
    configuration = load_config()
    print(configuration)
    run(configuration)

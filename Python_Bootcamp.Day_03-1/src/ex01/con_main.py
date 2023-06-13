import redis
import logging
import argparse
import json

badguy = []

logging.basicConfig(level=logging.INFO, format='%(message)s')


def lisner(red: redis.Redis):
    logging.info("Subscribe to ch1")
    try:
        subscriber = red.pubsub()
        subscriber.subscribe('ch1')
    except Exception as mes:
        logging.error(mes)
        return (False)
    logging.info("Subscribed")
    logging.info("Listening...")
    for mes in subscriber.listen():
        if mes is not None:
            if mes.get('type') == 'message':
                fixed(mes.get('data'))


def fixed(data: str):
    global badguy
    load: dict = json.load(data)
    order_from = load.get('message').get('from')
    order_to = load.get('message').get('to')
    amount = load.get('amount')

    if amount > 0 and order_to in badguy:
        load['metadata']['from'] = order_to
        load['metadata']['to'] = order_from

    logging.info(str(load))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", help="list of bad guys' account numbers, length = 10")
    args = parser.parse_args()
    if args.e:
        baddies = args.e
        baddies = baddies.split(',')
        for i in baddies:
            if i.isdigit():
                badguy.append(int(i))
            else:
                logging.error(
                    "Account should be all numeric \nE.g: 2222222222,444444444")
                exit(1)
    else:
        logging.info("Using default bad guys 2222222222,444444444")
        badguy = [2222222222, 4444444444]
    logging.info("Connection to redis started")
    try:
        red = redis.StrictRedis('localhost', 6379, decode_responses=True)
        logging.info("Redis connected")
    except:
        logging.error("Redis connection error")
        exit(1)

    while lisner(red):
        pass

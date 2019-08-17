import json
from game import Game


def get_players(event, context):

    game = Game()
    game.add_player('Oskar')
    game.add_player('Oliver')
    game.start()

    response = {
        "statusCode": 200,
        "body": json.dumps(game.players)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

import requests
from typing import List, Dict
from typing import Literal
import os

headers = {
    "x-api-key": os.getenv('api_key'),
}

domain = "https://api.bettingpros.com"

params = {
    "events": True,
    "key": "9070983c79ee4ccdabf8c1627",
    "user": "3852620",
    "user_type": "users",
    "stats": True,
    "pick_type": "sync:quick:expert:system",
}


def get_active_bets() -> List[Dict]:
    payload = {"status": "unscored", "sort": "relevance", **params}
    response = requests.get(domain + "/v3/picks", headers=headers, params=payload)
    data = response.json()
    bets = data["picks"]

    while next_url := data["_pagination"].get("next"):
        response = requests.get(domain + next_url, headers=headers, params=payload)
        if not response.ok:
            return bets
        data = response.json()
        bets += data["picks"]

    return bets


def get_bets_stats_in_time_interval(
    duration: Literal["D", "W", "M"], wager_filter: int
) -> List[Dict]:
    payload = {
        "status": "scored",
        "time_interval": f"1{duration}",
        "sort": "event_date",
        **params,
    }
    response = requests.get(domain + "/v3/picks", headers=headers, params=payload)
    data = response.json()
 
    num_of_bets, num_of_wins, num_of_losses = 0, 0, 0
    
    if len(data['picks']) < 1:
        return num_of_bets, num_of_wins, num_of_losses

    def process_bet(bet):
        nonlocal num_of_bets, num_of_wins, num_of_losses, wager_filter
        if bet["risk"]["units"] != wager_filter:
            return
        num_of_bets += 1
        if bet["result"]["result"] == "correct":
            num_of_wins += 1
        else:
            num_of_losses += 1

    for bet in data["picks"]:
        process_bet(bet)

    while next_url := data["_pagination"].get("next"):
        response = requests.get(domain + next_url, headers=headers)
        if not response.ok:
            return num_of_bets, num_of_wins, num_of_losses
        data = response.json()
        for bet in data["picks"]:
            process_bet(bet)
    return num_of_bets, num_of_wins, num_of_losses

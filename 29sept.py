"""
I got busted playing Genshin Impact at work... Some of my coworkers are pretty upset with me. I need your help.
I have a general idea of how upset each coworker is, but I need the overall sentiment of the team.

Here is your challenge: Given an object whose keys are strings representing the names of my coworkers, and whose values
are numbers representing how much they still like me, return whether or not I should quit before I get fired.

You should determine this by finding the average sentiment between all of my coworkers. If it is 5 or less,
tell me GTFO!. If it is more than 5, tell me You're gucci.

Oh, and if you see my boss, her score counts for double. I'll tell you her name as the second input.

Constraints:
Object values are a number such that 1 ≤ 10.
Keys will always be lowercase strings.

Test Cases:
With inputs {'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2,
'mr':0} and laura, return GTFO!
With inputs {'tim':1, 'jim':3, 'randy':9, 'sandy':6, 'andy':7, 'katie':6, 'laura':9, 'saajid':9, 'alex':9, 'john':9,
'mr':8} and katie, return You're gucci.
With inputs {'tim':2, 'jim':4, 'randy':0, 'sandy':5, 'andy':8, 'katie':6, 'laura':2, 'saajid':2, 'alex':3, 'john':2,
'mr':8} and john, return GTFO!
"""


# Take the mean of all the keys and return GTFO! if it is less than or equal to 5, otherwise return You're gucci.
def generate_overall_sentiment(coworkers, boss_name):
    sentiment = (sum(coworkers.values()) + coworkers[boss_name]) / len(coworkers)
    if sentiment <= 5:
        return "GTFO!"
    else:
        return "You're gucci."


if __name__ == "__main__":
    assert (
        generate_overall_sentiment(
            {
                "tim": 0,
                "jim": 2,
                "randy": 0,
                "sandy": 7,
                "andy": 0,
                "katie": 5,
                "laura": 1,
                "saajid": 2,
                "alex": 3,
                "john": 2,
                "mr": 0,
            },
            "laura",
        )
        == "GTFO!"
    )
    assert (
        generate_overall_sentiment(
            {
                "tim": 1,
                "jim": 3,
                "randy": 9,
                "sandy": 6,
                "andy": 7,
                "katie": 6,
                "laura": 9,
                "saajid": 9,
                "alex": 9,
                "john": 9,
                "mr": 8,
            },
            "katie",
        )
        == "You're gucci."
    )
    assert (
        generate_overall_sentiment(
            {
                "tim": 2,
                "jim": 4,
                "randy": 0,
                "sandy": 5,
                "andy": 8,
                "katie": 6,
                "laura": 2,
                "saajid": 2,
                "alex": 3,
                "john": 2,
                "mr": 8,
            },
            "john",
        )
        == "GTFO!"
    )

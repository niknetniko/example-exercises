import json

TESTCASES = 50

contexts = []
for i in range(TESTCASES):
    contexts.append({
        "testcases": [{
            "output": {
                "result": {
                    "value": {
                        "data": [
                            {"type": "number", "data": i - 1},
                            {"type": "number", "data": i + 1}
                        ],
                        "type": "sequence"
                    }
                }
            },
            "input": {
                "type": "function",
                "name": "remove",
                "arguments": [
                    {
                        "data": [
                            {"type": "number", "data": i - 1},
                            {"type": "number", "data": i},
                            {"type": "number", "data": i},
                            {"type": "number", "data": i + 1}
                        ],
                        "type": "sequence"
                    },
                    {
                        "data": i,
                        "type": "number"
                    }]
            }
        }]
    })

plan = {
    "tabs": [{
        "name": "Feedback",
        "runs": [{
            "contexts": contexts
        }]
    }]
}

f = open("../evaluation/full.tson", "w")

json.dump(plan, f, indent=2)

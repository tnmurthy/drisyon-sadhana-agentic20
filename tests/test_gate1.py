from src.agent import ReActAgent

def test_gate1_loop_termination():
    agent = ReActAgent(max_steps=3)
    res1 = agent.step({})
    assert res1["status"] == "CONTINUE"
    res2 = agent.step({})
    assert res2["status"] == "CONTINUE"
    res3 = agent.step({})
    assert res3["status"] == "HALTED"
    assert res3["reason"] == "MAX_STEPS_EXCEEDED"

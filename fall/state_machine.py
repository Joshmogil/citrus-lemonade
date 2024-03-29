from statemachine import StateMachine, State

class Ant(StateMachine):
    "A traffic light machine"
    green = State(initial=True)
    yellow = State()
    red = State()
    cycle = (
        green.to(yellow)
        | yellow.to(red)
        | red.to(green)
    )

    def before_cycle(self, event: str, source: State, target: State, message: str = ""):
        message = ". " + message if message else ""
        return f"Running {event} from {source.id} to {target.id}{message}"
    
    def on_enter_red(self):
        print("Don't move.")

    def on_exit_red(self):
        print("Go ahead!")

if __name__ == "__main__":
    sm = Ant()

    print(sm.allowed_events)
    print(sm.current_state)
    print(sm.cycle())
    print(sm.current_state)
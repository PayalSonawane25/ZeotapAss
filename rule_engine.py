import ast

class RuleEngine:
    def __init__(self):
        self.rules = {}  # Dictionary to store rules by name

    def create_rule(self, rule_name, rule_expr):
        """Create and store a new rule by its name and expression."""
        try:
            # Parse the expression to check if it is valid
            ast.parse(rule_expr)
            self.rules[rule_name] = rule_expr
            print(f"Rule '{rule_name}' created successfully.")
        except SyntaxError:
            raise ValueError(f"Invalid rule expression: {rule_expr}")

    def evaluate_rule(self, rule_name, parameters):
        """Evaluate a stored rule using provided parameters."""
        if rule_name not in self.rules:
            raise ValueError(f"Rule {rule_name} not found.")
        
        rule_expr = self.rules[rule_name]
        # Compile the rule into Python code and evaluate it
        try:
            rule_code = compile(rule_expr, "<string>", "eval")
            result = eval(rule_code, {}, parameters)
            print(f"Evaluation of rule '{rule_name}': {result}")
            return result
        except Exception as e:
            raise ValueError(f"Error evaluating rule {rule_name}: {e}")

    def display_rules(self):
        """Display all created rules."""
        if not self.rules:
            print("No rules available.")
        else:
            print("Stored Rules:")
            for rule_name, rule_expr in self.rules.items():
                print(f"{rule_name}: {rule_expr}")

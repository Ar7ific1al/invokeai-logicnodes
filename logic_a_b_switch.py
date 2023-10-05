from .baseinvocation import (
    BaseInvocation,
    InputField,
    InvocationContext,
    invocation
)

from .primitives import (
    IntegerOutput,
    FloatOutput
)

@invocation(
    "ab_switch_int", title="A B Switch (Integer)", tags=["logic", "switch", "integer"], category="logic", version="1.0.0"
)
class ABSwitchInt(BaseInvocation):
    """Switch between A and B for output"""

    switch: bool = InputField(default=False, description="Output A if off, B if on")
    a:      int = InputField(description = "Input A")
    b:      int = InputField(description = "Input B")

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value = self.b if self.switch else self.a)

@invocation(
    "ab_switch_float", title="A B Switch (Float)", tags=["logic", "switch", "float"], category="logic", version="1.0.0"
)
class ABSwitchFloat(BaseInvocation):
    """Switch between A and B for output"""

    switch: bool = InputField(default=False, description="Output A if off, B if on")
    a:      float = InputField(description = "Input A")
    b:      float = InputField(description = "Input B")

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value = self.b if self.switch else self.a)
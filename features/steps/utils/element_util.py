from behave.runner import Context


class ElementUtil:

    @classmethod
    def is_err_in_console_log(cls, context: Context, err_msg: str) -> bool:
        return any(msg for msg in context.console_log if err_msg in msg)

    @classmethod
    def element_visibility_by_id(cls, context: Context, elem_id: str) -> bool:
        return bool(context.helper.find_by_id(elem_id).is_displayed())

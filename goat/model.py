from behave import model


class Match(model.Match):
    def run(self, context):
        """We have to overwrite this method because we don't want an implicit context
        """
        args = []
        kwargs = {}
        for arg in self.arguments:
            if arg.name is not None:
                kwargs[arg.name] = arg.value
            else:
                args.append(arg.value)

        with context.user_mode():
            self.func(*args, **kwargs)
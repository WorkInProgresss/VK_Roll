import shlex
from argparse import ArgumentParser, SUPPRESS
from vk_client import GroupEventType


class CmdParserExit(Exception):
    pass


class CmdParser(ArgumentParser):

    def __init__(self, *args, **kwargs):
        super(CmdParser, self).__init__(*args, add_help=False, **kwargs)
        self._msg_buff = ''

        self.add_argument(
            '-h',
            action='help',
            default=SUPPRESS,
            help='show this help message'
        )

    def _print_message(self, message, file=None):
        self._msg_buff += message

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message)

        msg, self._msg_buff = self._msg_buff, ''

        raise CmdParserExit(msg)


class CmdHandler:

    def __init__(self, bot=None, prefix='$ ', version='0.0.1'):
        self.bot = bot

        self.prefix = prefix
        self.root_parser = CmdParser(
            prog=prefix
        )
        self.subparsers = self.root_parser.add_subparsers(
            parser_class=CmdParser
        )

        if bot is not None:
            self.init_bot(bot)

        self.root_parser.add_argument(
            '-V',
            action='version',
            default=SUPPRESS,
            version=version,
            help='show bot version number'
        )

    def init_bot(self, bot):
        self.bot = bot
        self.enable()

    def add(self, func, name=None, args=None, pass_msg=False):
        if name is None:
            name = func.__name__.replace('_', '-')

        if args is None:
            args = {}

        parser = self.subparsers.add_parser(
            name=name,
            description=func.__doc__
        )

        for arg, params in args.items():
            parser.add_argument(arg, **params)

        parser.set_defaults(_func=func, _pass_msg=pass_msg)

    def __call__(self, *args, **kwargs):
        """
        Decorator version of `self.add`.
        """
        def registering_wrapper(func):
            self.add(func, *args, **kwargs)
            return func

        return registering_wrapper

    def msg_is_cmd(self, msg):
        return msg.text.startswith(self.prefix)

    def enable(self):

        @self.bot.on([GroupEventType.MESSAGE_NEW])
        def handle_cmd(msg):
            if not self.msg_is_cmd(msg):
                return

            args_list = shlex.split(msg.text.lstrip(self.prefix))

            try:
                ns = self.root_parser.parse_args(args_list)

            except CmdParserExit as e:
                response = str(e) or 'Unable to parse a command.'

            else:
                try:
                    kwargs = {
                        k.replace('-', '_'): v
                        for k, v in vars(ns).items()
                        if not k.startswith('_')
                    }

                    if ns._pass_msg:
                        kwargs['msg'] = msg

                    response = ns._func(**kwargs)

                except Exception as e:
                    response = str(e)

            if response:
                self.bot.vk.Message.send(msg.sender, response)

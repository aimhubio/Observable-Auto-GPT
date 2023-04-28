from typing import Optional
import json
import copy
from aim import Run, Text
from aim.ext.resource.configs import DEFAULT_SYSTEM_TRACKING_INT


class AimCallback:
    """
    AimCallback callback function.

    Args:
        repo (:obj:`str`, optional): Aim repository path or Repo object to which Run object is bound.
            If skipped, default Repo is used.
        experiment_name (:obj:`str`, optional): Sets Run's `experiment` property. 'default' if not specified.
            Can be used later to query runs/sequences.
        system_tracking_interval (:obj:`int`, optional): Sets the tracking interval in seconds for system usage
            metrics (CPU, Memory, etc.). Set to `None` to disable system metrics tracking.
        log_system_params (:obj:`bool`, optional): Enable/Disable logging of system params such as installed packages,
            git info, environment variables, etc.
        capture_terminal_logs (:obj:`bool`, optional): Enable/Disable logging of terminal input/outputs.
        log_keys: (:obj:`bool`, optional) Triggers key(e.g. openai_api_key) tracking.
    """

    def __init__(
        self,
        repo: Optional[str] = None,
        experiment_name: Optional[str] = None,
        system_tracking_interval: Optional[int] = DEFAULT_SYSTEM_TRACKING_INT,
        log_system_params: Optional[bool] = True,
        capture_terminal_logs: Optional[bool] = True,
        log_keys: Optional[bool] = False,
    ):
        self.repo = repo
        self.experiment_name = experiment_name
        self.system_tracking_interval = system_tracking_interval
        self.log_system_params = log_system_params
        self.capture_terminal_logs = capture_terminal_logs
        self.log_keys = log_keys
        self._run = None
        self._run_hash = None

    def track(self, logs, context, step=None):
        for k, v in logs.items():
            if isinstance(v, list):
                if len(v) == 1:
                    v = v[0]
                else:
                    raise NotImplementedError(f"number of items in {k} are more than 1")
            self._run.track(v, k, step=step, context=context, epoch=self.epoch)

    def track_text(self, text, name, step=1, context=None):
        self._run.track(Text(text), name=name, step=step, context=context)

    @property
    def experiment(self):
        if not self._run:
            self.setup()
        return self._run

    def setup(self, args=None):
        if not self._run:
            if self._run_hash:
                self._run = Run(
                    self._run_hash,
                    repo=self.repo,
                    system_tracking_interval=self.system_tracking_interval,
                    log_system_params=self.log_system_params,
                    capture_terminal_logs=self.capture_terminal_logs,
                )
            else:
                self._run = Run(
                    repo=self.repo,
                    experiment=self.experiment_name,
                    system_tracking_interval=self.system_tracking_interval,
                    log_system_params=self.log_system_params,
                    capture_terminal_logs=self.capture_terminal_logs,
                )
                self._run_hash = self._run.hash

        # Log config parameters
        if args:
            for key, arg in args.items():
                arg = copy.copy(arg)
                try:
                    self._run.set(key, arg)
                except TypeError:
                    self._run.set(key, self._set(arg))

    def _set(self, args):
        args = args.__dict__
        keys = list(args.keys())
        for key in keys:
            if not self.log_keys and key.endswith("_key"):
                args.pop(key)
                continue
            try:
                json.dumps(args[key])
            except TypeError:
                args.pop(key)
        return args

    def close(self):
        self.__del__()

    def __del__(self):
        if self._run and self._run.active:
            self._run.close()

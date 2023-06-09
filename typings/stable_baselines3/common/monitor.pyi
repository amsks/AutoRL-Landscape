import gym
import numpy as np
# import pandas
from _typeshed import Incomplete
from stable_baselines3.common.type_aliases import GymObs, GymStepReturn
from typing import dict, List, Optional, Tuple, Union

class Monitor(gym.Wrapper):
    EXT: str
    t_start: Incomplete
    results_writer: Incomplete
    reset_keywords: Incomplete
    info_keywords: Incomplete
    allow_early_resets: Incomplete
    rewards: Incomplete
    needs_reset: bool
    episode_returns: Incomplete
    episode_lengths: Incomplete
    episode_times: Incomplete
    total_steps: int
    current_reset_info: Incomplete
    def __init__(self, env: gym.Env, filename: Optional[str] = ..., allow_early_resets: bool = ..., reset_keywords: Tuple[str, ...] = ..., info_keywords: Tuple[str, ...] = ...) -> None: ...
    # def reset(self, **kwargs) -> GymObs: ...
    def step(self, action: Union[np.ndarray, int]) -> GymStepReturn: ...
    def close(self) -> None: ...
    def get_total_steps(self) -> int: ...
    def get_episode_rewards(self) -> List[float]: ...
    def get_episode_lengths(self) -> List[int]: ...
    def get_episode_times(self) -> List[float]: ...

class LoadMonitorResultsError(Exception): ...

class ResultsWriter:
    file_handler: Incomplete
    logger: Incomplete
    def __init__(self, filename: str = ..., header: Optional[dict[str, Union[float, str]]] = ..., extra_keys: Tuple[str, ...] = ...) -> None: ...
    def write_row(self, epinfo: dict[str, Union[float, int]]) -> None: ...
    def close(self) -> None: ...

def get_monitor_files(path: str) -> List[str]: ...
# def load_results(path: str) -> pandas.DataFrame: ...

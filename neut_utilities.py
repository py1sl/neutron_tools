"""utility functions for use by neutron tools"""
from typing import Optional, Union, List, Dict, Any
from pathlib import Path
import logging
import logging.handlers
import sys
import os
import numpy as np
from datetime import datetime


class NeutronToolsLogger:
    """Centralized logging configuration for neutron tools"""
    
    def __init__(self) -> None:
        self.logger = logging.getLogger('nt_logger')
        self.logger.setLevel(logging.DEBUG)

    def setup_logging(
        self,
        log_file: Optional[Union[str, Path]] = None,
        console_level: str = 'INFO',
        file_level: str = 'DEBUG',
        log_format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ) -> logging.Logger:
        """Configure logging with console and optional file handlers.

        Args:
            log_file: Path to log file. If None, only console logging will be used.
                     Set to 'auto' for automatic date-based log file.
            console_level: Logging level for console output
            file_level: Logging level for file output
            log_format: Format string for log messages

        Returns:
            Configured logger instance
        """
        self.logger.handlers.clear()  # Remove any existing handlers

        # Create formatters
        formatter = logging.Formatter(log_format)

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(getattr(logging, console_level.upper()))
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # File handler (if requested)
        if log_file is not None:
            if log_file == 'auto':
                date_str = datetime.now().strftime('%Y%m%d')
                log_file = f'neutron_tools_{date_str}.log'
            
            file_handler = logging.handlers.RotatingFileHandler(
                log_file,
                maxBytes=10*1024*1024,  # 10MB
                backupCount=5
            )
            file_handler.setLevel(getattr(logging, file_level.upper()))
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        return self.logger

    def get_logger(self) -> logging.Logger:
        """Get the configured logger instance"""
        if not self.logger.handlers:
            self.setup_logging()
        return self.logger


def setup_ntlogger(
    log_file: Optional[Union[str, Path]] = None,
    console_level: str = 'INFO',
    file_level: str = 'DEBUG'
) -> logging.Logger:
    """Legacy function maintained for compatibility.
    Sets up the neutron tools logger with specified configuration.

    Args:
        log_file: Path to log file. If None, only console logging will be used.
                 Default is 'auto' for automatic date-based log file.
        console_level: Logging level for console output
        file_level: Logging level for file output

    Returns:
        Configured logger instance
    """
    logger_instance = NeutronToolsLogger()
    return logger_instance.setup_logging(
        log_file=log_file,
        console_level=console_level,
        file_level=file_level
    )


def write_lines(path, lines):
    """ writes lines list to file at path """
    with open(path, 'w') as f:
        for line in lines:
            f.write(f"{line}\n")


def get_lines(path):
    """ reads file at path and returns a list with 1 entry per line """
    with open(path) as f:
        lines = f.read().splitlines()
    return lines


def find_line(text, lines, num):
    """ finds first index of the line in lines where the text is present
        in the first num characters
    """
    for i, line in enumerate(lines):
        if line[:num] == text:
            return i
    raise ValueError(f"'{text}' not found within the first {num} characters of any line.")


def string_cleaner(text):
    """ returns cleaned up line """
    text = text.strip()
    text = " ".join(text.split())
    return text


def string_clean_and_split(text, spliter=" "):
    """ clean and split text on spaces """
    text = string_cleaner(text)
    text_list = text.split(spliter)
    return text_list


def find_ind(data, sub):
    """ finds first index in data which contains sub string """
    for i, s in enumerate(data):
        if sub in s:
            return i
    raise ValueError(f"The substring - '{sub}' was not found.")


def find_first_non_zero(val_list):
    """ finds the first non zero value in a list and returns its position """
    arr = np.asarray(val_list)
    nonzero_indices = np.nonzero(arr)[0]
    if nonzero_indices.size > 0:
        return int(nonzero_indices[0])
    else:
        return None


def find_first_zero(val_list):
    """ finds the first zero value in a list and returns its position """
    arr = np.asarray(val_list)
    zero_indices = np.where(arr == 0)[0]
    if zero_indices.size > 0:
        return int(zero_indices[0])
    else:
        return None


def get_list_dimensions(lst):
    """ finds dimensions of a list or list of lists etc"""
    if not isinstance(lst, list):
        return []

    dimensions = []
    while isinstance(lst, list):
        dimensions.append(len(lst))
        lst = lst[0] if len(lst) > 0 else []

    return dimensions


def text_replace(fname, old_string, new_string):
    """ replaces strings in place in a file """

    # replace string
    with open(fname, 'r') as file:
        data = file.read()
        data = data.replace(old_string, new_string)

    # output modified data
    with open(fname, 'w') as file:
        file.write(data)


def is_same_value(v1, v2, tolerance=1e-6):
    """ check if two float values are effectively equal within tolerance."""
    return abs(v1 - v2) < tolerance

##########################################################################
# NSAp - Copyright (C) CEA, 2016
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# System import
import unittest
import sys

# COMPATIBILITY: since python 3.3 mock is included in unittest module
python_version = sys.version_info
if python_version[:2] <= (3, 3):
    import mock
    from mock import patch
else:
    import unittest.mock as mock
    from unittest.mock import patch

# Pyfsl import
from pyfsl.utils.filetools import fslreorient2std, apply_mask


class Fslreorient2std(unittest.TestCase):
    """ Test the FSL reorient the image to standard:
    'pyfsl.utils.filetools.fslreorient2std'
    """
    def setUp(self):
        """ Run before each test - the mock_popen will be available and in the
        right state in every test<something> function.
        """
        # Mocking popen
        self.popen_patcher = patch("pyfsl.wrapper.subprocess.Popen")
        self.mock_popen = self.popen_patcher.start()
        mock_process = mock.Mock()
        attrs = {
            "communicate.return_value": ("mock_OK", "mock_NONE"),
            "returncode": 0
        }
        mock_process.configure_mock(**attrs)
        self.mock_popen.return_value = mock_process

        # Mocking set environ
        self.env_patcher = patch(
            "pyfsl.wrapper.FSLWrapper._fsl_version_check")
        self.mock_env = self.env_patcher.start()
        self.mock_env.return_value = {}

        # Define function parameters
        self.kwargs = {
            "input_image": "/my/path/mock_input_image",
            "output_image": "/my/path/mock_output_image",
            "fslconfig": "/my/path/mock_shfile",
        }

    def tearDown(self):
        """ Run after each test.
        """
        self.popen_patcher.stop()
        self.env_patcher.stop()

    @mock.patch("pyfsl.utils.filetools.os.path.isfile")
    def test_badfileerror_raise(self, mock_isfile):
        """Bad input file -> raise valueError.
        """
        # Set the mocked functions returned values
        mock_isfile.side_effect = [False]

        # Test execution
        self.assertRaises(ValueError, fslreorient2std, **self.kwargs)

    @mock.patch("pyfsl.utils.filetools.os.path.isfile")
    def test_normal_execution(self, mock_isfile):
        """ Test the normal behaviour of the function.
        """
        # Set the mocked function returned values.
        mock_isfile.side_effect = [True]

        # Test execution
        fslreorient2std(**self.kwargs)

        self.assertEqual([
            mock.call(["which", "fslreorient2std"],
                      env={}, stderr=-1, stdout=-1),
            mock.call(["fslreorient2std",
                      self.kwargs["input_image"],
                      self.kwargs["output_image"]],
                      env={}, stderr=-1, stdout=-1)],
            self.mock_popen.call_args_list)
        self.assertEqual(len(self.mock_env.call_args_list), 1)


class FslApplyMask(unittest.TestCase):
    """ Test the FSL apply mask:
    'pyfsl.utils.filetools.apply_mask'
    """
    def setUp(self):
        """ Run before each test - the mock_popen will be available and in the
        right state in every test<something> function.
        """
        # Mocking popen
        self.popen_patcher = patch("pyfsl.wrapper.subprocess.Popen")
        self.mock_popen = self.popen_patcher.start()
        mock_process = mock.Mock()
        attrs = {
            "communicate.return_value": ("mock_OK", "mock_NONE"),
            "returncode": 0
        }
        mock_process.configure_mock(**attrs)
        self.mock_popen.return_value = mock_process

        # Mocking set environ
        self.env_patcher = patch(
            "pyfsl.wrapper.FSLWrapper._fsl_version_check")
        self.mock_env = self.env_patcher.start()
        self.mock_env.return_value = {}

        # Define function parameters
        self.kwargs = {
            "input_image": "/my/path/mock_input_image",
            "mask_image": "/my/path/mock_mask_image",
            "output_image": "/my/path/mock_output_image",
            "fslconfig": "/my/path/mock_shfile",
        }

    def tearDown(self):
        """ Run after each test.
        """
        self.popen_patcher.stop()
        self.env_patcher.stop()

    def test_badfileerror_raise(self):
        """Bad input file -> raise valueError.
        """
        # Test execution
        self.assertRaises(ValueError, apply_mask, **self.kwargs)

    @mock.patch("pyfsl.utils.filetools.os.path.isfile")
    def test_normal_execution(self, mock_isfile):
        """ Test the normal behaviour of the function.
        """
        # Set the mocked function returned values.
        mock_isfile.side_effect = [True, True]

        # Test execution
        apply_mask(**self.kwargs)

        self.assertEqual([
            mock.call(["which", "fslmaths"],
                      env={}, stderr=-1, stdout=-1),
            mock.call(["fslmaths",
                       self.kwargs["input_image"],
                       "-mas", self.kwargs["mask_image"],
                       self.kwargs["output_image"]],
                      env={}, stderr=-1, stdout=-1)],
            self.mock_popen.call_args_list)
        self.assertEqual(len(self.mock_env.call_args_list), 1)


if __name__ == "__main__":
    unittest.main()

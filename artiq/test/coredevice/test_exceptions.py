import unittest
import artiq.coredevice.exceptions as exceptions

from artiq.experiment import *
from artiq.test.hardware_testbench import ExperimentCase
from artiq.language.embedding_map import EmbeddingMap
from artiq.coredevice.core import test_exception_id_sync
from numpy import int32

"""
Test sync in exceptions raised between host and kernel
Check `artiq.compiler.embedding` and `artiq::firmware::ksupport::eh_artiq`

Considers the following two cases:
    1) Exception raised on kernel and passed to host
    2) Exception raised in a host function called from kernel
Ensures same exception is raised on both kernel and host in either case
"""

exception_names = EmbeddingMap().string_map


@nac3
class _TestExceptionSync(EnvExperiment):
    def build(self):
        self.setattr_device("core")
    
    @rpc
    def _raise_exception_host(self, id: int32):
        exn = exception_names[id].split('.')[-1].split(':')[-1]
        exn = getattr(exceptions, exn)
        raise exn

    @kernel
    def raise_exception_host(self, id: int32):
        self._raise_exception_host(id)

    @kernel
    def raise_exception_kernel(self, id: int32):
        test_exception_id_sync(id)


class ExceptionTest(ExperimentCase):
    def test_raise_exceptions_kernel(self):
        exp = self.create(_TestExceptionSync)
        
        for id, name in exception_names.items():
            name = name.split('.')[-1].split(':')[-1]
            with self.assertRaises(getattr(exceptions, name)) as ctx:
                exp.raise_exception_kernel(id)
            self.assertEqual(str(ctx.exception).strip("'"), name)
            
            
    def test_raise_exceptions_host(self):
        exp = self.create(_TestExceptionSync)

        for id, name in exception_names.items():
            name = name.split('.')[-1].split(':')[-1]
            with self.assertRaises(getattr(exceptions, name)) as ctx:
                exp.raise_exception_host(id)

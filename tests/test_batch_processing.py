import unittest
from murphy.batch_processing import Batches
from murphy.data_loader import DataLoader
from tests import CommonTestSetup


class BatchProcessingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data_path, _ = CommonTestSetup.set_data_dir_path()

    def test_process_in_batches(self):
        files_lst = DataLoader.get_files_list(self.data_path)
        results = Batches.process_in_batches(files_lst, read_func=DataLoader._read_compressed_bz2_json_file,
                                             func_to_apply=len, verbose=False)
        print(results)
        self.assertTrue(set(results.values()) == {5758, 5480})

    def test_process_in_batches_generator(self):
        files_lst = DataLoader.get_files_list(self.data_path)
        results = Batches.process_in_batches_generator(file_iterator=files_lst,
                                                       read_func=DataLoader._read_compressed_bz2_json_file,
                                                       func_to_apply=len)
        results = list(results)
        self.assertTrue(set(results), {5758, 5480})

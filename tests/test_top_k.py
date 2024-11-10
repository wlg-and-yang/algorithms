import pytest
from algorithms.arrays import top_k

# # 测试用例
# def test_top_k_with_positive_numbers():
#     assert top_k([1, 2, 3, 2, 3, 4, 4, 4], 2) == [4, 4]

# def test_top_k_with_negative_numbers():
#     assert top_k([-1, -2, -3, -2, -3, -4, -4, -4], 2) == [-1, -2]

# def test_top_k_with_single_element():
#     assert top_k([1], 1) == [1]

# # @pytest.mark.skip(reason="skip--------------")
# def test_top_k_with_empty_list():
#     assert top_k([], 1) == -1

# # @pytest.mark.skip(reason="skip--------------")
# def test_top_k_with_k_greater_than_unique_elements():
#     assert top_k([1, 2, 3], 5) == -1

# def test_top_k_with_k_zero():
#     assert top_k([1, 2, 3], 0) == []

# def test_top_k_with_all_elements_same():
#     assert top_k([1, 1, 1, 1], 2) == [1, 1]

# # @pytest.mark.skip(reason="skip--------------")
# # def test_top_k_with_k_negative():
# #     with pytest.raises(ValueError):
# #         top_k([1, 2, 3], -1)

# # 运行测试
# if __name__ == "__main__":
#     pytest.main()

import pytest
from algorithms.arrays import top_k

class TestTopK:
    # 测试用例
    def test_top_k_with_positive_numbers(self):
        assert top_k([1, 2, 3, 2, 3, 4, 4, 4], 2) == [4, 4]

    def test_top_k_with_negative_numbers(self):
        assert top_k([-1, -2, -3, -2, -3, -4, -4, -4], 2) == [-1, -2]

    def test_top_k_with_single_element(self):
        assert top_k([1], 1) == [1]

    def test_top_k_with_empty_list(self):
        assert top_k([], 1) == -1

    def test_top_k_with_k_greater_than_unique_elements(self):
        assert top_k([1, 2, 3], 5) == -1

    def test_top_k_with_k_zero(self):
        assert top_k([1, 2, 3], 0) == []

    def test_top_k_with_all_elements_same(self):
        assert top_k([1, 1, 1, 1], 2) == [1, 1]

    

# 运行测试
if __name__ == "__main__":
    pytest.main()

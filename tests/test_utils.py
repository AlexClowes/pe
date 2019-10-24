import utils


def test_is_palindrome():
    assert utils.is_palindrome(1234321) == True
    assert utils.is_palindrome(1234320) == False


def test_get_prime_factors():
    assert utils.get_prime_factors(60) == [2, 2, 3, 5]
    assert utils.get_prime_factors(73) == [73]
    assert utils.get_prime_factors(1) == []


def test_get_factors():
    assert sorted(utils.get_factors(60)) == [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
    assert sorted(utils.get_factors(1)) == [1]


def test_get_first_n_primes():
    assert utils.get_first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_get_primes_up_to_n():
    assert list(utils.get_primes_up_to_n(10)) == [2, 3, 5, 7]
    assert list(utils.get_primes_up_to_n(4)) == [2, 3]


def test_is_prime():
    assert utils.is_prime(1) == False
    assert utils.is_prime(2) == True
    assert utils.is_prime(7) == True
    assert utils.is_prime(899) == False


def test_gcd():
    assert utils.gcd(1, 10) == 1
    assert utils.gcd(899, 1073) == 29


def test_get_partition_count():
    assert utils.get_partition_count(-1) == 0
    assert utils.get_partition_count(0) == 1
    assert utils.get_partition_count(10) == 42
    assert utils.get_partition_count(50) == 204226

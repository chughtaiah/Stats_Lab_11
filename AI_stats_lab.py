def zero_rho_covariance_check(n=100000):
    """
    Generate samples with rho=0 and verify covariance is near zero.
    """

    x, y = generate_joint_gaussian_samples(
        n=n,
        rho=0,
        seed=0
    )

    cov_matrix = sample_covariance_matrix(x, y)
    covariance = cov_matrix[0, 1]

    return bool(abs(covariance) < 0.05)


def nonzero_rho_covariance_check(n=100000):
    """
    Generate samples with rho=0.6 and verify covariance is close to 3.6.
    """

    x, y = generate_joint_gaussian_samples(
        n=n,
        rho=0.6,
        seed=0
    )

    cov_matrix = sample_covariance_matrix(x, y)
    covariance = cov_matrix[0, 1]

    return bool(abs(covariance - 3.6) < 0.15)

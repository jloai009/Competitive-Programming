class Solution
{
public:
  int countPrimes(int n)
  {
    if (n < 2)
      return 0;
    vector<bool> primes = vector<bool>(n, true);
    const int UPPER_BOUND = pow(n, 0.5) + 1;
    primes[0] = false;
    primes[1] = false;

    for (int i = 2; i < UPPER_BOUND; i++)
    {
      if (primes[i])
      {
        for (int j = i * i; j < n; j += i)
        {
          primes[j] = false;
        }
      }
    }

    int result = 0;
    for (int i = 0; i < n; i++)
    {
      if (primes[i])
        result++;
    }
    return result;
  }
};

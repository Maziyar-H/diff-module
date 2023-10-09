{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(array([ 1.        ,  0.80901699,  0.30901699, -0.30901699, -0.80901699,\n",
      "       -1.        ]), array([[  8.5       , -10.47213595,   2.89442719,  -1.52786405,\n",
      "          1.10557281,  -0.5       ],\n",
      "       [  2.61803399,  -1.17082039,  -2.        ,   0.89442719,\n",
      "         -0.61803399,   0.2763932 ],\n",
      "       [ -0.7236068 ,   2.        ,  -0.17082039,  -1.61803399,\n",
      "          0.89442719,  -0.38196601],\n",
      "       [  0.38196601,  -0.89442719,   1.61803399,   0.17082039,\n",
      "         -2.        ,   0.7236068 ],\n",
      "       [ -0.2763932 ,   0.61803399,  -0.89442719,   2.        ,\n",
      "          1.17082039,  -2.61803399],\n",
      "       [  0.5       ,  -1.10557281,   1.52786405,  -2.89442719,\n",
      "         10.47213595,  -8.5       ]]))\n"
     ]
    }
   ],
   "source": [
    "# this environment contains ipykernel numpy scipy matplotlib\n",
    "#This is a code to generate a chebichev derivative matrix\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "\n",
    "def d_matrix(N):\n",
    "    \"\"\"Generate a matrix that uses chebyshev spectral methods to take derivative'\"\"\"\n",
    "    x = np.array([0.0 for i in range(N+1)])\n",
    "    if N==0:\n",
    "        x = 1\n",
    "    else:\n",
    "        for i in range(0,N+1):\n",
    "            x[i] = np.cos(np.pi*(i/N)) \n",
    "        \n",
    "        c = np.array([1.0 for i in range(N+1)])\n",
    "        c[0] = 2\n",
    "        c[N] = 2\n",
    "        cI = np.array([np.power(-1,i) for i in range(N+1)])\n",
    "        c = np.multiply(c,cI)[np.newaxis]\n",
    "        X = np.tile(x,(N+1,1))\n",
    "        dX = X.transpose() - X\n",
    "        c1 = np.divide(1,c)\n",
    "        c2 = np.matmul(c.T,c1)\n",
    "        D1 = dX+np.identity(N+1)\n",
    "        DD = np.divide(c2,D1)\n",
    "        sDD = (DD.T).sum(axis=0)\n",
    "        sDD_1 =  np.diag(sDD)\n",
    "        D = DD - sDD_1\n",
    "        \n",
    "    return x,D\n",
    "\n",
    "    \n",
    "print(d_matrix(5)) \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This function creates a differentiation matrix based on Chebychev polynomials. \n",
    "$N$ is the polynomoal degree. \n",
    "Collocation points are at: $x_j = cos(\\frac{\\pi j}{N})$ with $j = 0,1,2 ... N$.\n",
    "The produced matrix is $N+1\\times N+1$.\n",
    "The diff. matrix is $D^N_{ij} = \\frac{C_i (-1)^{(i+j)}}{c_j (x_i -x_j)}$"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

bool isPalindrome(int x){
    if (x < 10 && x > -1) {
        return true;
    }
    if (x < 0) {
        return false;
    }

    int temp = x;
    long final = 0;

    while (temp > 0) {
        final *= 10;
        final += temp % 10;
        temp /= 10; 
    }
    return final == x;
}

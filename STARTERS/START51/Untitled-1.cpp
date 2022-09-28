int noOfWays(int input1)
{
    int first=1;
    int second=2;
    if(input1==1)
    return 1;
    if(input1==2)
    return 2;
    int third;
    for(int i=3;i<=input1;i++)
    {
        third=(first+second)%1000000007;
        first=second%1000000007;
        second=third%1000000007;
    }
    return third;
}
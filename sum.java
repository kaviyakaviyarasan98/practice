import java.util.Scanner;
class sum
{
public static void main(String[] args)
{
Scanner sc=new Scanner(System.in);
int n,i;
int sum=0;
n=sc.nextInt();
for(i=1;i<=n;i++)
{
sum=sum+i;
}
System.out.println(sum);
}
}
#include <stdio.h>


int main(void)
 {
	
int num;
	
int i=2;
	
scanf("%d",&num);
	
for(i=2;i<num;i++)
	
{
		
if(num%i==0)
		
{
			
printf("not a prime");
		
exit(0);
	
}
		
	
}
	
printf("prime");
	
return 0;

}

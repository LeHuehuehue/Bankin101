
double max, min, number;
int count = 0;

cout << "Enter 0:";
cin >> number;
max = number;
min = number;

if(count != 0)
    count++;

while(number != 0)
{
    cin >> number;
    if(number > max)
    {
        max = number;
    }
    else if (number < min)
        min = number;
    
    count++;
}

cout << "There were " << count << " numbers inputed.\n";
return 0;
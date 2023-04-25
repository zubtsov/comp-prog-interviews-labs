program problem1639;
uses Math;
var
        m,n:byte;
begin
        readln(m,n);
        if (n=1) or (m=1) then
                if (odd(max(n,m))) then
                        write('[second]=:]')
                else
                        write('[:=[first]')

        else if odd(m*n-1) then {(m-1)*(n-1) << неверно}
                write('[:=[first]')
        else
                write('[second]=:]')
end.
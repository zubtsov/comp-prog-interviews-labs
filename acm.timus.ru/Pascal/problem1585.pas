program problem1585;
uses Math;
const
        names:array[1..3] of string[16] = ('Emperor Penguin', 'Macaroni Penguin', 'Little Penguin');
        counts:array[1..3] of word = (0,0,0);
var
        i,n:integer;
        str:string[16];
begin
        readln(n);

        for i:=1 to n do begin
                readln(str);
                case str[1] of
                        'E':counts[1]:=counts[1]+1;
                        'M':counts[2]:=counts[2]+1;
                else
                        counts[3]:=counts[3]+1
                end;
        end;
        if (counts[1]>counts[2]) and (counts[1]>counts[3]) then
                write(names[1])
        else if (counts[2]>counts[1]) and (counts[2]>counts[3]) then
                write(names[2])
        else
                write(names[3])
end.
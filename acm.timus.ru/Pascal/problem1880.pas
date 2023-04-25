program problem1880;
type
        mas = array[1..4000] of longint;
var
        a,b,c:mas;
        al,bl,cl:word;

        i,counter:integer;

function BinarySearch(const key:integer; massiv:mas; l,h:integer):boolean;
var
        m:integer;
begin
        while (l<h) do begin
                m:=(l+h) div 2;
                if (massiv[m] >= key) then
                        h:=m
                else
                        l:=m+1;
        end;

        if (massiv[h] = key) then
                BinarySearch:=true
        else
                BinarySearch:=false

end;

begin
        readln(al);

        for i:=1 to al do
                read(a[i]);

        readln(bl);

        for i:=1 to bl do
                read(b[i]);

        readln(cl);

        for i:=1 to cl do
                read(c[i]);

        counter:=0;

        for i:=1 to cl do
                if (BinarySearch(c[i],b,1,bl)) and (BinarySearch(c[i], a, 1, al)) then
                        counter:=counter+1;
        write(counter)
end.

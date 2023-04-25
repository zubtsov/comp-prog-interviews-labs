program problem1005;
uses Math;
type
        mas=array[1..20] of longint;
var
        sa,sb,diff:longint;
        n:byte;
        a,b:mas;
        i,j:integer;

function summ(const A:mas):longint;
var
        temp:longint;
        i:integer;
begin
        temp:=0;
        for i:=1 to High(A) do
                temp:=temp+A[i];
        summ:=temp
end;

function find_elem(const A:mas; key:longint):integer;
var
        temp:longint;
        i,f:integer;
begin
        temp:=abs(key-A[1]);
        f:=1;
        for i:=1 to High(A) do
                if (abs(key-A[i]) < temp) then begin
                        temp:=abs(key-A[i]);
                        f:=i;
                end;
        find_elem:=f;
end;

begin
        readln(n);
        for i:=1 to n do read(a[i]);
        for i:=1 to n do b[i]:=0;

        for i:=1 to n do begin {уточнить необходимое количество итераций, оптимизировать}
        sa:=summ(a);
        sb:=summ(b);
        diff:=abs(sa-sb) div 2;
        if (sa<sb) then begin
                j:=find_elem(b,diff);
                if (b[j]<>0) then begin
                a[j]:=b[j];
                b[j]:=0 end
        end
        else begin
                j:=find_elem(a,diff);
                if (a[j]<>0) then begin
                b[j]:=a[j];
                a[j]:=0 end;
        end end;
        writeln(abs(sa-sb));
end.
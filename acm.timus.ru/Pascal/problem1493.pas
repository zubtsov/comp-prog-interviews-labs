program problem1493;
var
        n:longint;
        s:string[6];

function conv(n:longint):string;
var
        s:string[6];
begin
        Str(n,s);
        while (length(s)<6) do
                s:='0'+s;
        conv:=s
end;

function lucky(n:longint):boolean;
var
        s:string;
begin
        s:=conv(n);
        if (Ord(s[1])+Ord(s[2])+Ord(s[3])=Ord(s[4])+Ord(s[5])+Ord(s[6])) then
                lucky:=true
        else
                lucky:=false
end;

begin
        readln(s);
        val(s,n);
        if (lucky(n+1)) or (lucky(n-1)) then
                write('Yes')
        else
                write('No')
end.
program problem1009;
var
        N,K:byte;

function pow(X,Y:byte):longint;
begin
        if (Y>0) then
                pow:=X*pow(X,Y-1)
        else
                pow:=1
end;

function zero_count(N,K:byte):longint;
begin
        if (N>3) then
                zero_count:=pow(K,N-2)+(K-1)*(zero_count(N-1,K)+zero_count(N-2,K))
        else if (N>2) then
                zero_count:=2*(K-1)+1
        else if (N>1) then
                zero_count:=1
        else
                zero_count:=0
end;

begin
        readln(N,K);
        writeln((K-1)*(pow(K,N-1)-zero_count(N-1,K)));
end.
program problem1001;
var i,n:integer;
	a:array[1..100000000] of extended;
begin
	n:=0;

while not seekeof do begin
	inc(n);
	read(a[n])
end;

	for i:=n downto 1 do
		writeln(sqrt(a[i]):0:4)
end.
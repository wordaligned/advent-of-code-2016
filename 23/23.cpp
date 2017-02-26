#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

namespace
{
vector<vector<string>> commands(istream & in)
{
	vector<vector<string>> cmds;
	for (string line; getline(cin, line);)
	{
		vector<string> cmd(3);
		string op, arg1, arg;
		stringstream ss(line + " !");
		ss >> cmd[0] >> cmd[1] >> cmd[2];
		cmds.push_back(cmd);
	}
	return cmds;
}

long value(map<string, long> regs, string v)
{
	auto reg = regs.find(v);
	return reg == regs.end() ? strtol(v.c_str(), nullptr, 0): regs[v];
}

void tgl(vector<string> & cmd)
{
	if      (cmd[0] == "inc") cmd[0] = "dec";
	else if (cmd[0] == "dec") cmd[0] = "inc";
	else if (cmd[0] == "jnz") cmd[0] = "cpy";
	else if (cmd[0] == "cpy") cmd[0] = "jnz";
}

void run(vector<vector<string>> & cmds, map<string, long> & regs)
{
	for (auto pos = 0ul; pos >= 0 && pos < cmds.size();)
	{
		auto cmd = cmds[pos];
		auto op = cmd[0];
		if (op == "tgl")
		{
			auto tpos = pos + value(regs, cmd[1]);
			if (tpos >= 0 && tpos < cmds.size())
			{
				tgl(cmds[tpos]);
			}
			++pos;
		}
		else if (op == "cpy")
		{
			regs[cmd[2]] = value(regs, cmd[1]);
			++pos;
		}
		else if (op == "inc")
		{
			++regs[cmd[1]];
			++pos;
		}
		else if (op == "dec")
		{
			--regs[cmd[1]];
			++pos;
		}
		else if (op == "jnz")
		{
			auto test = value(regs, cmd[1]);
			auto step = value(regs, cmd[2]);
			pos += test ? step : 1;
		}
		else
		{
			cerr << "Invalid op " << op << '\n';
		}
	}
}

} // anonymous namespace

int main(int argc, char * argv[])
{
	auto regs = map<string, long>();
	regs["a"] = strtol(argv[1], nullptr, 0);
	vector<vector<string>> cmds = commands(cin);
	run(cmds, regs);
	cout << regs["a"] << endl;
	return 0;
}

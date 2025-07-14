
#include <iostream>


#include "Colors.h"
#include "MainWin.h"
#include <gtkmm/application.h>
#include <giomm.h>
#include "CmdLine.h"

Colors* Colors::_instance = NULL;


bool handleCmdLine(int argc, char* argv[])
{
	CmdLine* cmd = new CmdLine();
	bool result = cmd->handleArguments(argc,argv);
	
	delete cmd;
	return result;
}

int main(int argc, char* argv[])
{
	Gio::init();
	
	if (argc > 1)
	{
		if (handleCmdLine(argc, argv))
			return 0;
	}
	
	auto app = Gtk::Application::create(argc, argv, "com.scangine.filelock");
  
	MainWin window;

	int result = app->run(window);
	Colors::free();
	return result;
}



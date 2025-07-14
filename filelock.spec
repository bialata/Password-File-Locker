Name:           filelock
Version:        1.0
Release:        1%{?dist}
Summary:        Secure and strong file encryption using a password

License:        Freeware
URL:            https://scangine.com/encryption/
Source0:	filelock
Source1:	com.scangine.filelock.png
Source2:	com.scangine.filelock.desktop
Source3:	license.txt

%description
Secure and strong file encryption using a password.

The password is used to encrypt the selected file so it can only be unlocked by entering the same password.

You can easily encrypt important documents and files to protect the information when storing them or sending them over the internet. You can use different passwords for different files. When encrypting files the original file is not deleted but only encrypted copy is created. It is up to you to decide what to do with both original and encrypted files and to remember your password. If you forget the password the information CAN NOT BE RESTORED.

%prep
#cp /home/pop/projects/Releases/FileLock/filelock %{_sourcedir}/filelock
#cp /home/pop/projects/Releases/FileLock/com.scangine.filelock.png %{_sourcedir}/com.scangine.filelock.png
#cp /home/pop/projects/Releases/FileLock/com.scangine.filelock.desktop %{_sourcedir}/com.scangine.filelock.desktop
#cp /home/pop/projects/Releases/FileLock/license.txt %{_sourcedir}/license.txt

%build
# nothing here


%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/icons/hicolor/48x48/
mkdir -p %{buildroot}/usr/share/licenses/filelock/
mkdir -p %{buildroot}/usr/share/applications/
install -m 755  %{SOURCE0} %{buildroot}/usr/bin/filelock
cp %{SOURCE1} %{buildroot}/usr/share/icons/hicolor/48x48/com.scangine.filelock.png
cp %{SOURCE3} %{buildroot}/usr/share/licenses/filelock/license.txt
cp %{SOURCE2} %{buildroot}/usr/share/applications/com.scangine.filelock.desktop

%files
%license license.txt
/usr/bin/filelock
/usr/share/icons/hicolor/48x48/com.scangine.filelock.png
/usr/share/applications/com.scangine.filelock.desktop

%changelog
* Sun Jul 13 2025 biala
- 

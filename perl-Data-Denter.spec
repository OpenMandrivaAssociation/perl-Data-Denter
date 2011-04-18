%define upstream_name    Data-Denter
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    An alternative to Data::Dumper and Storable
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(YAML)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The main problem with Data::Dumper (one of my all-time favorite modules) is
that you have to use 'eval()' to deserialize the data you've dumped. This
is great if you can trust the data you're evaling, but horrible if you
can't. A good alternative is Storable.pm. It can safely thaw your frozen
data. But if you want to read/edit the frozen data, you're out of luck,
because Storable uses a binary format. Even Data::Dumper's output can be a
little cumbersome for larger data objects.

Enter Data::Denter.

Data::Denter is yet another Perl data serializer/deserializer. It formats
nested data structures in an indented fashion. It is optimized for human
readability/editability, safe deserialization, and (eventually) speed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



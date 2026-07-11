%global tl_name invoice
%global tl_revision 48359

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Generate invoices
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/invoice
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package may be used for generating invoices. The package can deal
with invisible expense items and deductions; output may be presented in
any of 10 different languages. A long-standing bug has been removed.
Numbers now can show the comma as decimal separator. The package depends
on the fp, calc and siunitx for its calculations.


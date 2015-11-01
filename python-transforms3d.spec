%global modname transforms3d

Name:           python-%{modname}
Version:        0.2.1
Release:        2%{?dist}
Summary:        3 dimensional spatial transformations

License:        BSD
URL:            http://matthew-brett.github.io/transforms3d/
Source0:        https://github.com/matthew-brett/transforms3d/archive/%{version}/%{modname}-%{version}.tar.gz
# https://github.com/matthew-brett/transforms3d/pull/7
Patch0:         0001-pull-fixes-from-nipy-nipy.patch
BuildRequires:  git-core
BuildArch:      noarch

%description
Code to convert between various geometric transformations.

* Composing rotations / zooms / shears / translations into affine matrix;
* Decomposing affine matrix into rotations / zooms / shears / translations;
* Conversions between different representations of rotations, including:
** 3x3 Rotation matrices;
** Euler angles;
** quaternions.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
# Test deps
BuildRequires:  python-nose
BuildRequires:  numpy
Requires:       numpy
Recommends:     sympy

%description -n python2-%{modname}
Code to convert between various geometric transformations.

* Composing rotations / zooms / shears / translations into affine matrix;
* Decomposing affine matrix into rotations / zooms / shears / translations;
* Conversions between different representations of rotations, including:
** 3x3 Rotation matrices;
** Euler angles;
** quaternions.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
# Test deps
BuildRequires:  python3-nose
BuildRequires:  python3-numpy
Requires:       python3-numpy
Recommends:     python3-sympy

%description -n python3-%{modname}
Code to convert between various geometric transformations.

* Composing rotations / zooms / shears / translations into affine matrix;
* Decomposing affine matrix into rotations / zooms / shears / translations;
* Conversions between different representations of rotations, including:
** 3x3 Rotation matrices;
** Euler angles;
** quaternions.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -S git

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests-%{python2_version} -v
nosetests-%{python3_version} -v

%files -n python2-%{modname}
%license LICENSE
%doc README.rst AUTHORS
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%doc README.rst AUTHORS
%{python3_sitelib}/%{modname}*

%changelog
* Sun Nov 01 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.1-2
- Backport patch from upstream (nipy/nipy)

* Sun Nov 01 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.1-1
- Initital package

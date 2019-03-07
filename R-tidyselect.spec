#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tidyselect
Version  : 0.2.5
Release  : 14
URL      : https://cran.r-project.org/src/contrib/tidyselect_0.2.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tidyselect_0.2.5.tar.gz
Summary  : Select from a Set of Strings
Group    : Development/Tools
License  : GPL-3.0
Requires: R-tidyselect-lib
Requires: R-Rcpp
Requires: R-dplyr
Requires: R-purrr
BuildRequires : R-Rcpp
BuildRequires : R-dplyr
BuildRequires : R-purrr
BuildRequires : buildreq-R

%description
It makes it easy to implement select-like functions in your own
    packages in a way that is consistent with other 'tidyverse'
    interfaces for selection.

%package lib
Summary: lib components for the R-tidyselect package.
Group: Libraries

%description lib
lib components for the R-tidyselect package.


%prep
%setup -q -c -n tidyselect

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539274894

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1539274894
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyselect
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyselect
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyselect
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library tidyselect|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyselect/DESCRIPTION
/usr/lib64/R/library/tidyselect/INDEX
/usr/lib64/R/library/tidyselect/Meta/Rd.rds
/usr/lib64/R/library/tidyselect/Meta/features.rds
/usr/lib64/R/library/tidyselect/Meta/hsearch.rds
/usr/lib64/R/library/tidyselect/Meta/links.rds
/usr/lib64/R/library/tidyselect/Meta/nsInfo.rds
/usr/lib64/R/library/tidyselect/Meta/package.rds
/usr/lib64/R/library/tidyselect/NAMESPACE
/usr/lib64/R/library/tidyselect/NEWS.md
/usr/lib64/R/library/tidyselect/R/tidyselect
/usr/lib64/R/library/tidyselect/R/tidyselect.rdb
/usr/lib64/R/library/tidyselect/R/tidyselect.rdx
/usr/lib64/R/library/tidyselect/help/AnIndex
/usr/lib64/R/library/tidyselect/help/aliases.rds
/usr/lib64/R/library/tidyselect/help/paths.rds
/usr/lib64/R/library/tidyselect/help/tidyselect.rdb
/usr/lib64/R/library/tidyselect/help/tidyselect.rdx
/usr/lib64/R/library/tidyselect/html/00Index.html
/usr/lib64/R/library/tidyselect/html/R.css
/usr/lib64/R/library/tidyselect/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyselect/libs/tidyselect.so
/usr/lib64/R/library/tidyselect/libs/tidyselect.so.avx2
/usr/lib64/R/library/tidyselect/libs/tidyselect.so.avx512

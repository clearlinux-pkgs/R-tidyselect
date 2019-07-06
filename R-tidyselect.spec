#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tidyselect
Version  : 0.2.5
Release  : 22
URL      : https://cran.r-project.org/src/contrib/tidyselect_0.2.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tidyselect_0.2.5.tar.gz
Summary  : Select from a Set of Strings
Group    : Development/Tools
License  : GPL-3.0
Requires: R-tidyselect-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-dplyr
Requires: R-glue
Requires: R-purrr
Requires: R-rlang
BuildRequires : R-Rcpp
BuildRequires : R-dplyr
BuildRequires : R-glue
BuildRequires : R-purrr
BuildRequires : R-rlang
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
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562200114

%install
export SOURCE_DATE_EPOCH=1562200114
rm -rf %{buildroot}
export LANG=C.UTF-8
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tidyselect || :


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
/usr/lib64/R/library/tidyselect/tests/testthat.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-inds-combine.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-select-helpers.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-vars-pull.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-vars-rename.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-vars-select.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-vars.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyselect/libs/tidyselect.so

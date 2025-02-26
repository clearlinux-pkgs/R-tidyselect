#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-tidyselect
Version  : 1.2.1
Release  : 58
URL      : https://cran.r-project.org/src/contrib/tidyselect_1.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tidyselect_1.2.1.tar.gz
Summary  : Select from a Set of Strings
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-glue
Requires: R-lifecycle
Requires: R-rlang
Requires: R-vctrs
Requires: R-withr
BuildRequires : R-cli
BuildRequires : R-glue
BuildRequires : R-lifecycle
BuildRequires : R-rlang
BuildRequires : R-vctrs
BuildRequires : R-withr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
makes it easy to implement select-like functions in your own packages
    in a way that is consistent with other 'tidyverse' interfaces for
    selection.

%prep
%setup -q -n tidyselect
pushd ..
cp -a tidyselect buildavx2
popd
pushd ..
cp -a tidyselect buildavx512
popd
pushd ..
cp -a tidyselect buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740104066

%install
export SOURCE_DATE_EPOCH=1740104066
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyselect/DESCRIPTION
/usr/lib64/R/library/tidyselect/INDEX
/usr/lib64/R/library/tidyselect/LICENSE
/usr/lib64/R/library/tidyselect/Meta/Rd.rds
/usr/lib64/R/library/tidyselect/Meta/features.rds
/usr/lib64/R/library/tidyselect/Meta/hsearch.rds
/usr/lib64/R/library/tidyselect/Meta/links.rds
/usr/lib64/R/library/tidyselect/Meta/nsInfo.rds
/usr/lib64/R/library/tidyselect/Meta/package.rds
/usr/lib64/R/library/tidyselect/Meta/vignette.rds
/usr/lib64/R/library/tidyselect/NAMESPACE
/usr/lib64/R/library/tidyselect/NEWS.md
/usr/lib64/R/library/tidyselect/R/tidyselect
/usr/lib64/R/library/tidyselect/R/tidyselect.rdb
/usr/lib64/R/library/tidyselect/R/tidyselect.rdx
/usr/lib64/R/library/tidyselect/doc/index.html
/usr/lib64/R/library/tidyselect/doc/syntax.R
/usr/lib64/R/library/tidyselect/doc/syntax.Rmd
/usr/lib64/R/library/tidyselect/doc/syntax.html
/usr/lib64/R/library/tidyselect/doc/tidyselect.R
/usr/lib64/R/library/tidyselect/doc/tidyselect.Rmd
/usr/lib64/R/library/tidyselect/doc/tidyselect.html
/usr/lib64/R/library/tidyselect/help/AnIndex
/usr/lib64/R/library/tidyselect/help/aliases.rds
/usr/lib64/R/library/tidyselect/help/paths.rds
/usr/lib64/R/library/tidyselect/help/tidyselect.rdb
/usr/lib64/R/library/tidyselect/help/tidyselect.rdx
/usr/lib64/R/library/tidyselect/html/00Index.html
/usr/lib64/R/library/tidyselect/html/R.css
/usr/lib64/R/library/tidyselect/tests/testthat.R
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/eval-bool.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/eval-c.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/eval-relocate.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/eval-rename.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/eval-select.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/eval-walk.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/helpers-misc.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/helpers-pattern.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/helpers-vector.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/helpers-where.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/helpers.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/lifecycle-deprecated.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/proxy.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/vars-pull.md
/usr/lib64/R/library/tidyselect/tests/testthat/_snaps/vars.md
/usr/lib64/R/library/tidyselect/tests/testthat/helper-tidyselect.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-eval-bool.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-eval-c.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-eval-relocate.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-eval-rename.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-eval-select.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-eval-walk.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-helpers-misc.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-helpers-pattern.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-helpers-vector.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-helpers-where.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-helpers.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-lifecycle-deprecated.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-proxy.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-sets.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-vars-pull.R
/usr/lib64/R/library/tidyselect/tests/testthat/test-vars.R

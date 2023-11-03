#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tidyselect
Version  : 1.2.0
Release  : 54
URL      : https://cran.r-project.org/src/contrib/tidyselect_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tidyselect_1.2.0.tar.gz
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

%description
makes it easy to implement select-like functions in your own packages
    in a way that is consistent with other 'tidyverse' interfaces for
    selection.

%prep
%setup -q -n tidyselect
cd %{_builddir}/tidyselect

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665447286

%install
export SOURCE_DATE_EPOCH=1665447286
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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

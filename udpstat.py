  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>udpstat/udpstat.py at master · pzolee/udpstat · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <link rel="assets" href="https://a248.e.akamai.net/assets.github.com/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="QLTqe98zMTa2MSSj6J0u+FD6OrW1P0nKdbHW3jUmZ9Q=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-a4c524f2138ecc4dd5bf9b8a6b1517bf38aa7b65.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-90ab6d28026c957cc4eb3342b1512f4c4737ede5.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-5c60c478b1e0f90d149f11ed15aa52edd2996882.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-bea1759cc95fdb5c7e9e75865d7f5f52cde816c0.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="ae58be9616684df1f6944f16d25aa1d4">

        <link data-pjax-transient rel='permalink' href='/pzolee/udpstat/blob/b38cce914c9c4080e5198b85f8f48c9c86ae06b6/udpstat.py'>
    <meta property="og:title" content="udpstat"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/pzolee/udpstat"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/4c807453c54722b28245518d32f02d48?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="udpstat - Collecting data from the state of UDP buffers"/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="pzolee/udpstat"/>

    <meta name="description" content="udpstat - Collecting data from the state of UDP buffers" />


    <meta content="2269659" name="octolytics-dimension-user_id" /><meta content="pzolee" name="octolytics-dimension-user_login" /><meta content="5657726" name="octolytics-dimension-repository_id" /><meta content="pzolee/udpstat" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="5657726" name="octolytics-dimension-repository_network_root_id" /><meta content="pzolee/udpstat" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/pzolee/udpstat/commits/master.atom" rel="alternate" title="Recent Commits to udpstat:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob windows vis-public env-production  ">
    <div id="wrapper">

      
      
      

      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">Github</a>

    <div class="header-actions">
      <a class="button primary" href="/signup">Sign up</a>
      <a class="button" href="/login?return_to=%2Fpzolee%2Fudpstat%2Fblob%2Fmaster%2Fudpstat.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">


      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="http://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">
  <a href="/search/advanced" class="advanced-search-icon tooltipped downwards command-bar-search" id="advanced_search" title="Advanced search"><span class="octicon octicon-gear "></span></a>

  <input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
      data-repo="pzolee/udpstat"
      data-branch="master"
      data-sha="c75eca73379d66826e54c8e1e0ec9d8103cc1d2c"
  >

    <input type="hidden" name="nwo" value="pzolee/udpstat" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

  <div class="divider-vertical"></div>

</form>
    </div>

  </div>
</div>


      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2Fpzolee%2Fudpstat"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="octicon octicon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/pzolee/udpstat/stargazers">
        0
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2Fpzolee%2Fudpstat"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/pzolee/udpstat/network" class="social-count">
        1
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-octicon octicon-repo"></span>
                <span class="author vcard">
                  <a href="/pzolee" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">pzolee</span>
                  </a></span> /
                <strong><a href="/pzolee/udpstat" class="js-current-repository">udpstat</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/pzolee/udpstat/pulse" class="js-selected-navigation-item " data-selected-links="pulse /pzolee/udpstat/pulse" rel="nofollow"><span class="octicon octicon-pulse"></span></a></li>
    <li><a href="/pzolee/udpstat" class="js-selected-navigation-item selected" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /pzolee/udpstat">Code</a></li>
    <li><a href="/pzolee/udpstat/network" class="js-selected-navigation-item " data-selected-links="repo_network /pzolee/udpstat/network">Network</a></li>
    <li><a href="/pzolee/udpstat/pulls" class="js-selected-navigation-item " data-selected-links="repo_pulls /pzolee/udpstat/pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/pzolee/udpstat/issues" class="js-selected-navigation-item " data-selected-links="repo_issues /pzolee/udpstat/issues">Issues <span class='counter'>0</span></a></li>



    <li><a href="/pzolee/udpstat/graphs" class="js-selected-navigation-item " data-selected-links="repo_graphs repo_contributors /pzolee/udpstat/graphs">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/pzolee/udpstat/tags" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_tags /pzolee/udpstat/tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="octicon octicon-git-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item selected">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/pzolee/udpstat/blob/master/udpstat.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <div class="select-menu-no-results">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/pzolee/udpstat" class="selected js-selected-navigation-item tabnav-tab" data-selected-links="repo_source /pzolee/udpstat">Files</a></li>
    <li><a href="/pzolee/udpstat/commits/master" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_commits /pzolee/udpstat/commits/master">Commits</a></li>
    <li><a href="/pzolee/udpstat/branches" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_branches /pzolee/udpstat/branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:c50f8f604d6bca5e93100acade1d789e -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:c50f8f604d6bca5e93100acade1d789e -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/pzolee/udpstat" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">udpstat</span></a></span></span><span class="separator"> / </span><strong class="final-path">udpstat.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="udpstat.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
        </div>

      <a href="/pzolee/udpstat/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/pzolee/udpstat/contributors/master/udpstat.py">
          Fetching contributors…

          <div class="participation">
            <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
            <p class="loader-error">Cannot retrieve contributors at this time</p>
          </div>
        </div>

    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/pzolee/udpstat/blob/b38cce914c9c4080e5198b85f8f48c9c86ae06b6/udpstat.py" data-title="udpstat/udpstat.py at master · pzolee/udpstat · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="octicon octicon-file-text"></b></span>
                <span class="mode" title="File Mode">executable file</span>
                  <span>170 lines (143 sloc)</span>
                <span>7.534 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/pzolee/udpstat/raw/master/udpstat.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/pzolee/udpstat/blame/master/udpstat.py" class="button minibutton ">Blame</a>
                  <a href="/pzolee/udpstat/commits/master/udpstat.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/python</span></div><div class='line' id='LC2'><span class="c"># vim: sts=4 ts=8 et ai</span></div><div class='line' id='LC3'><br/></div><div class='line' id='LC4'><span class="sd">&#39;&#39;&#39; UDP buffer size (RX, TX) and dropped packages statistics program, written by PZolee (pzoleex @ freemail.hu), 2012&#39;&#39;&#39;</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="kn">import</span> <span class="nn">signal</span></div><div class='line' id='LC7'><span class="kn">import</span> <span class="nn">time</span></div><div class='line' id='LC8'><span class="kn">from</span> <span class="nn">re</span> <span class="kn">import</span> <span class="n">search</span></div><div class='line' id='LC9'><span class="kn">from</span> <span class="nn">optparse</span> <span class="kn">import</span> <span class="n">OptionParser</span></div><div class='line' id='LC10'><span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">datetime</span></div><div class='line' id='LC11'><span class="kn">from</span> <span class="nn">sys</span> <span class="kn">import</span> <span class="nb">exit</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><br/></div><div class='line' id='LC14'><span class="k">def</span> <span class="nf">signal_handler</span><span class="p">(</span><span class="n">signal</span><span class="p">,</span> <span class="n">frame</span><span class="p">):</span></div><div class='line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Exiting&quot;</span></div><div class='line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ofile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Maximum tx queue: &quot;</span> <span class="o">+</span> <span class="n">q_res</span> <span class="o">%</span> <span class="p">({</span><span class="s">&#39;in_byte&#39;</span><span class="p">:</span> <span class="n">max_tx</span><span class="p">,</span> <span class="s">&#39;in_kbyte&#39;</span><span class="p">:</span> <span class="n">max_tx</span> <span class="o">/</span> <span class="mi">1024</span><span class="p">,</span> <span class="s">&#39;in_mbyte&#39;</span><span class="p">:</span> <span class="n">max_tx</span> <span class="o">/</span> <span class="mi">1048576</span><span class="p">})</span></div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Maximum rx queue: &quot;</span> <span class="o">+</span> <span class="n">q_res</span> <span class="o">%</span> <span class="p">({</span><span class="s">&#39;in_byte&#39;</span><span class="p">:</span> <span class="n">max_rx</span><span class="p">,</span> <span class="s">&#39;in_kbyte&#39;</span><span class="p">:</span> <span class="n">max_rx</span> <span class="o">/</span> <span class="mi">1024</span><span class="p">,</span> <span class="s">&#39;in_mbyte&#39;</span><span class="p">:</span> <span class="n">max_rx</span> <span class="o">/</span> <span class="mi">1048576</span><span class="p">})</span></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Dropped packages: </span><span class="si">%s</span><span class="s"> &quot;</span> <span class="o">%</span> <span class="n">drops</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><span class="n">signal</span><span class="o">.</span><span class="n">signal</span><span class="p">(</span><span class="n">signal</span><span class="o">.</span><span class="n">SIGINT</span><span class="p">,</span> <span class="n">signal_handler</span><span class="p">)</span></div><div class='line' id='LC28'><br/></div><div class='line' id='LC29'><span class="n">udp_input</span> <span class="o">=</span> <span class="s">&#39;/proc/net/udp&#39;</span></div><div class='line' id='LC30'><span class="sd">&#39;&#39;&#39;  sl  local_address rem_address   st tx_queue rx_queue tr tm-&gt;when retrnsmt   uid  timeout inode ref pointer drops</span></div><div class='line' id='LC31'><span class="sd">   8: 00000000:02BA 00000000:0000 07 00000000:00000000 00:00000000 00000000     0        0 4515 2 ffff8802a94c0000 0</span></div><div class='line' id='LC32'><span class="sd">  59: 00000000:E16D 00000000:0000 07 00000000:00000000 00:00000000 00000000     0        0 4528 2 ffff8802a94b0000 0</span></div><div class='line' id='LC33'><span class="sd">  61: 00000000:006F 00000000:0000 07 00000000:00000000 00:00000000 00000000     0        0 4316 2 ffff8802a9498000 0</span></div><div class='line' id='LC34'><span class="sd">  73: 00000000:EC7B 00000000:0000 07 00000000:00000000 00:00000000 00000000     0        0 16701920 2 ffff8802a949cac0 0</span></div><div class='line' id='LC35'><span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><span class="n">usage</span> <span class="o">=</span> <span class="s">&quot;usage: %prog [options] port&quot;</span></div><div class='line' id='LC38'><span class="n">desc</span> <span class="o">=</span> <span class="s">&quot;UDP buffer size (RX, TX) and dropped packages statistics program, written by PZolee (pzoleex @ freemail.hu), 2012&quot;</span></div><div class='line' id='LC39'><span class="n">parser</span> <span class="o">=</span> <span class="n">OptionParser</span><span class="p">(</span><span class="n">usage</span><span class="p">,</span> <span class="n">description</span> <span class="o">=</span> <span class="n">desc</span><span class="p">,</span> <span class="n">version</span> <span class="o">=</span> <span class="s">&quot;%prog version: 1.0&quot;</span><span class="p">)</span></div><div class='line' id='LC40'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-o&quot;</span><span class="p">,</span> <span class="s">&quot;--output&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&quot;filename&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;The name of the output file&quot;</span><span class="p">,</span> <span class="n">metavar</span> <span class="o">=</span> <span class="s">&quot;&lt;filename&gt;&quot;</span><span class="p">)</span></div><div class='line' id='LC41'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-r&quot;</span><span class="p">,</span> <span class="s">&quot;--rx&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Measure the size of RX(incoming) buffer&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&quot;store_true&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&quot;rx&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC42'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-t&quot;</span><span class="p">,</span> <span class="s">&quot;--tx&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Measure the size of TX(outgoing) buffer&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&quot;store_true&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&quot;tx&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC43'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-d&quot;</span><span class="p">,</span> <span class="s">&quot;--drops&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Measure the number of dropped packages for RX and TX buffers&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&quot;store_true&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&quot;drops&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC44'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-b&quot;</span><span class="p">,</span> <span class="s">&quot;--displayed-blocks&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&quot;block_size&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;The displayed block size for the TX, RX queues. Possible values: B, K, M, all; default: </span><span class="si">%d</span><span class="s">efault&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s">&quot;all&quot;</span><span class="p">)</span></div><div class='line' id='LC45'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-l&quot;</span><span class="p">,</span> <span class="s">&quot;--listened-port-type&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;The type of the listened port, default: </span><span class="si">%d</span><span class="s">efault&quot;</span><span class="p">,</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&quot;store&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&quot;listened&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s">&quot;local&quot;</span><span class="p">,</span> <span class="n">metavar</span> <span class="o">=</span> <span class="s">&quot;&lt;local|remote&gt;&quot;</span><span class="p">)</span></div><div class='line' id='LC47'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-f&quot;</span><span class="p">,</span> <span class="s">&quot;--freq&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;The time between two polls in sec, default: </span><span class="si">%d</span><span class="s">efault&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&quot;store&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&quot;freq&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&quot;float&quot;</span><span class="p">)</span></div><div class='line' id='LC48'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-u&quot;</span><span class="p">,</span> <span class="s">&quot;--run-time&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;The running time if given. Default: untill CTRL+C&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&quot;store&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&quot;runtime&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&quot;int&quot;</span><span class="p">)</span></div><div class='line' id='LC49'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-c&quot;</span><span class="p">,</span> <span class="s">&quot;--csv&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Generate CSV output format&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&quot;store_true&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&quot;csv&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC50'><br/></div><div class='line' id='LC51'><span class="p">(</span><span class="n">opts</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span></div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'><span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">block_size</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span> <span class="o">==</span> <span class="s">&quot;B&quot;</span><span class="p">:</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">q_res</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%(in_byte)s</span><span class="s"> bytes; &quot;</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">q_header</span> <span class="o">=</span> <span class="s">&quot;{0} in bytes&quot;</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csv_res</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%(in_byte)s</span><span class="s">;&quot;</span></div><div class='line' id='LC57'><span class="k">elif</span> <span class="n">opts</span><span class="o">.</span><span class="n">block_size</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span> <span class="o">==</span> <span class="s">&quot;K&quot;</span><span class="p">:</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">q_res</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%(in_kbyte)s</span><span class="s"> KB; &quot;</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">q_header</span> <span class="o">=</span> <span class="s">&quot;{0} in kilobytes&quot;</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csv_res</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%(in_kbyte)s</span><span class="s">;&quot;</span></div><div class='line' id='LC61'><span class="k">elif</span> <span class="n">opts</span><span class="o">.</span><span class="n">block_size</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span> <span class="o">==</span> <span class="s">&quot;M&quot;</span><span class="p">:</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">q_res</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%(in_mbyte)s</span><span class="s"> MB; &quot;</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">q_header</span> <span class="o">=</span> <span class="s">&quot;{0} in megabytes;&quot;</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csv_res</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%(in_mbyte)s</span><span class="s">;&quot;</span></div><div class='line' id='LC65'><span class="k">else</span><span class="p">:</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">q_res</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%(in_byte)s</span><span class="s"> bytes, </span><span class="si">%(in_kbyte)s</span><span class="s"> KB, </span><span class="si">%(in_mbyte)s</span><span class="s"> MB; &quot;</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">q_header</span> <span class="o">=</span> <span class="s">&quot;{0} in bytes;{0} in kilobytes;{0} in megabytes;&quot;</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csv_res</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%(in_byte)s</span><span class="s">;</span><span class="si">%(in_kbyte)s</span><span class="s">;</span><span class="si">%(in_mbyte)s</span><span class="s">;&quot;</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'><span class="k">if</span> <span class="ow">not</span> <span class="n">opts</span><span class="o">.</span><span class="n">rx</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">opts</span><span class="o">.</span><span class="n">tx</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">opts</span><span class="o">.</span><span class="n">drops</span><span class="p">:</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#If no limits, display all counters</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">use_all_counter</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC73'><span class="k">else</span><span class="p">:</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">use_all_counter</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC75'><br/></div><div class='line' id='LC76'><span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Port is required!&quot;</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">print_help</span><span class="p">()</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC80'><br/></div><div class='line' id='LC81'><span class="n">hexport</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%x</span><span class="s">&quot;</span> <span class="o">%</span> <span class="nb">int</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span></div><div class='line' id='LC82'><span class="k">print</span> <span class="s">&quot;Start collecting RX and TX queue statistics information and dropped packages result for port (</span><span class="si">%s</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC83'><br/></div><div class='line' id='LC84'><span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">filename</span><span class="p">:</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ofile</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">opts</span><span class="o">.</span><span class="n">filename</span><span class="p">,</span> <span class="s">&#39;wb&#39;</span><span class="p">)</span></div><div class='line' id='LC86'><br/></div><div class='line' id='LC87'><span class="n">is_header</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC88'><span class="n">header</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></div><div class='line' id='LC89'><span class="n">max_rx</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC90'><span class="n">max_tx</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'><span class="n">stime</span> <span class="o">=</span> <span class="n">atime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span></div><div class='line' id='LC93'><span class="k">while</span> <span class="n">stime</span> <span class="o">&gt;=</span> <span class="n">atime</span> <span class="o">-</span> <span class="n">opts</span><span class="o">.</span><span class="n">runtime</span><span class="p">:</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">udp_input</span><span class="p">,</span> <span class="s">&#39;rb&#39;</span><span class="p">)</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lines</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">readlines</span><span class="p">()</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">search</span><span class="p">(</span><span class="n">hexport</span><span class="p">,</span> <span class="n">item</span><span class="p">)</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">buffers</span> <span class="o">=</span> <span class="n">item</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">()</span> <span class="c"># 0:sl, 1:local_address, 2:rem_address, 3:st, 4:tx_queue rx_queue, 5:tr tm-&gt;when retrnsmt</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># 6:retrnsmt, 7:uid, 8:timeout, 9:inode, 10:ref, 11:pointer, 12:drops</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sl</span><span class="p">,</span> <span class="n">la</span><span class="p">,</span> <span class="n">ra</span><span class="p">,</span> <span class="n">st</span><span class="p">,</span> <span class="n">tx_rx</span><span class="p">,</span> <span class="n">tr</span><span class="p">,</span> <span class="n">retrnsmt</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">timeout</span><span class="p">,</span> <span class="n">inode</span><span class="p">,</span> <span class="n">ref</span><span class="p">,</span> <span class="n">pointer</span><span class="p">,</span> <span class="n">drops</span> <span class="o">=</span> <span class="n">buffers</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">listened</span> <span class="o">==</span> <span class="s">&#39;local&#39;</span> <span class="ow">and</span> <span class="n">search</span><span class="p">(</span><span class="n">la</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">],</span> <span class="n">hexport</span><span class="p">)</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># The local port does not match to the given local port</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;There is no matching port yet&quot;</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">opts</span><span class="o">.</span><span class="n">freq</span><span class="p">)</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">listened</span> <span class="o">==</span> <span class="s">&#39;remote&#39;</span> <span class="ow">and</span> <span class="n">search</span><span class="p">(</span><span class="n">ra</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">],</span> <span class="n">hexport</span><span class="p">)</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># The remote port does not match to the given remote port</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;There is no matching port yet&quot;</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">opts</span><span class="o">.</span><span class="n">freq</span><span class="p">)</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC112'><br/></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tx_queue</span><span class="p">,</span> <span class="n">rx_queue</span> <span class="o">=</span> <span class="n">tx_rx</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rx_queue</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">rx_queue</span><span class="p">,</span> <span class="mi">16</span><span class="p">)</span> <span class="c"># convert to dec</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tx_queue</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">tx_queue</span><span class="p">,</span> <span class="mi">16</span><span class="p">)</span> <span class="c"># convert to dec</span></div><div class='line' id='LC116'><br/></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">rx_queue</span> <span class="o">&gt;</span> <span class="n">max_rx</span><span class="p">:</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">max_rx</span> <span class="o">=</span> <span class="n">rx_queue</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tx_queue</span> <span class="o">&gt;</span> <span class="n">max_tx</span><span class="p">:</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">max_tx</span> <span class="o">=</span> <span class="n">tx_queue</span></div><div class='line' id='LC121'><br/></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">header</span> <span class="o">=</span> <span class="s">&quot;time;&quot;</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">res</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">isoformat</span><span class="p">()</span> <span class="o">+</span> <span class="s">&quot;;&quot;</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">tx</span> <span class="ow">or</span> <span class="n">use_all_counter</span><span class="p">:</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">csv</span><span class="p">:</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">res</span> <span class="o">=</span> <span class="n">res</span> <span class="o">+</span> <span class="n">csv_res</span> <span class="o">%</span> <span class="p">({</span><span class="s">&#39;in_byte&#39;</span><span class="p">:</span> <span class="n">tx_queue</span><span class="p">,</span> <span class="s">&#39;in_kbyte&#39;</span><span class="p">:</span> <span class="n">tx_queue</span> <span class="o">/</span> <span class="mi">1024</span><span class="p">,</span> <span class="s">&#39;in_mbyte&#39;</span><span class="p">:</span> <span class="n">tx_queue</span> <span class="o">/</span> <span class="mi">1048576</span><span class="p">})</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">is_header</span><span class="p">:</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">header</span> <span class="o">=</span> <span class="n">header</span> <span class="o">+</span> <span class="n">q_header</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s">&quot;tx&quot;</span><span class="p">)</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">res</span> <span class="o">=</span> <span class="n">res</span> <span class="o">+</span> <span class="s">&quot;tx queue: &quot;</span> <span class="o">+</span> <span class="n">q_res</span> <span class="o">%</span> <span class="p">({</span><span class="s">&#39;in_byte&#39;</span><span class="p">:</span> <span class="n">tx_queue</span><span class="p">,</span> <span class="s">&#39;in_kbyte&#39;</span><span class="p">:</span> <span class="n">tx_queue</span> <span class="o">/</span> <span class="mi">1024</span><span class="p">,</span> <span class="s">&#39;in_mbyte&#39;</span><span class="p">:</span> <span class="n">tx_queue</span> <span class="o">/</span> <span class="mi">1048576</span><span class="p">})</span></div><div class='line' id='LC131'><br/></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">rx</span> <span class="ow">or</span> <span class="n">use_all_counter</span><span class="p">:</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">csv</span><span class="p">:</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">res</span> <span class="o">=</span> <span class="n">res</span> <span class="o">+</span> <span class="n">csv_res</span> <span class="o">%</span> <span class="p">({</span><span class="s">&#39;in_byte&#39;</span><span class="p">:</span> <span class="n">rx_queue</span><span class="p">,</span> <span class="s">&#39;in_kbyte&#39;</span><span class="p">:</span> <span class="n">rx_queue</span> <span class="o">/</span> <span class="mi">1024</span><span class="p">,</span> <span class="s">&#39;in_mbyte&#39;</span><span class="p">:</span> <span class="n">rx_queue</span> <span class="o">/</span> <span class="mi">1048576</span><span class="p">})</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">is_header</span><span class="p">:</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">header</span> <span class="o">=</span> <span class="n">header</span> <span class="o">+</span> <span class="n">q_header</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s">&quot;rx&quot;</span><span class="p">)</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">res</span> <span class="o">=</span> <span class="n">res</span> <span class="o">+</span> <span class="s">&quot;rx queue: &quot;</span> <span class="o">+</span> <span class="n">q_res</span> <span class="o">%</span> <span class="p">({</span><span class="s">&#39;in_byte&#39;</span><span class="p">:</span> <span class="n">rx_queue</span><span class="p">,</span> <span class="s">&#39;in_kbyte&#39;</span><span class="p">:</span> <span class="n">rx_queue</span> <span class="o">/</span> <span class="mi">1024</span><span class="p">,</span> <span class="s">&#39;in_mbyte&#39;</span><span class="p">:</span> <span class="n">rx_queue</span> <span class="o">/</span> <span class="mi">1048576</span><span class="p">})</span></div><div class='line' id='LC139'><br/></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">drops</span> <span class="ow">or</span> <span class="n">use_all_counter</span><span class="p">:</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">csv</span><span class="p">:</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">res</span> <span class="o">=</span> <span class="n">res</span> <span class="o">+</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">;&quot;</span> <span class="o">%</span> <span class="n">drops</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">is_header</span><span class="p">:</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">header</span> <span class="o">=</span> <span class="n">header</span> <span class="o">+</span> <span class="s">&quot;dropped packages;&quot;</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">res</span> <span class="o">=</span> <span class="n">res</span> <span class="o">+</span> <span class="s">&quot;dropped packages: </span><span class="si">%s</span><span class="s">;&quot;</span> <span class="o">%</span> <span class="n">drops</span></div><div class='line' id='LC147'><br/></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">csv</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">is_header</span><span class="p">:</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">header</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">filename</span><span class="p">:</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ofile</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">header</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ofile</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">is_header</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC154'><br/></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">res</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">filename</span><span class="p">:</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ofile</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">res</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ofile</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC159'><br/></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">opts</span><span class="o">.</span><span class="n">freq</span><span class="p">)</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">runtime</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">atime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span></div><div class='line' id='LC163'><br/></div><div class='line' id='LC164'><span class="k">print</span> <span class="s">&quot;Maximum tx queue: &quot;</span> <span class="o">+</span> <span class="n">q_res</span> <span class="o">%</span> <span class="p">({</span><span class="s">&#39;in_byte&#39;</span><span class="p">:</span> <span class="n">max_tx</span><span class="p">,</span> <span class="s">&#39;in_kbyte&#39;</span><span class="p">:</span> <span class="n">max_tx</span> <span class="o">/</span> <span class="mi">1024</span><span class="p">,</span> <span class="s">&#39;in_mbyte&#39;</span><span class="p">:</span> <span class="n">max_tx</span> <span class="o">/</span> <span class="mi">1048576</span><span class="p">})</span></div><div class='line' id='LC165'><span class="k">print</span> <span class="s">&quot;Maximum rx queue: &quot;</span> <span class="o">+</span> <span class="n">q_res</span> <span class="o">%</span> <span class="p">({</span><span class="s">&#39;in_byte&#39;</span><span class="p">:</span> <span class="n">max_rx</span><span class="p">,</span> <span class="s">&#39;in_kbyte&#39;</span><span class="p">:</span> <span class="n">max_rx</span> <span class="o">/</span> <span class="mi">1024</span><span class="p">,</span> <span class="s">&#39;in_mbyte&#39;</span><span class="p">:</span> <span class="n">max_rx</span> <span class="o">/</span> <span class="mi">1048576</span><span class="p">})</span></div><div class='line' id='LC166'><span class="k">print</span> <span class="s">&quot;Dropped packages: </span><span class="si">%s</span><span class="s"> &quot;</span> <span class="o">%</span> <span class="n">drops</span></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'><span class="k">if</span> <span class="n">opts</span><span class="o">.</span><span class="n">filename</span><span class="p">:</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ofile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif" height="64" width="64">
</div>


        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="/about">About us</a></dd>
        <dd><a href="/blog">Blog</a></dd>
        <dd><a href="/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.04433s from fe17.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>
    <ul id="legal">
        <li><a href="/site/terms">Terms of Service</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/pzolee/udpstat/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="octicon octicon-remove-close ajax-error-dismiss"></a>
    </div>

    
    <span id='server_response_time' data-time='0.04470' data-host='fe17'></span>
    
  </body>
</html>


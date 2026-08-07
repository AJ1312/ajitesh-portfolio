css_append = """

/* Responsive Overrides for Strict Grid */
@media screen and (max-width: 940px) {
  .newspaper-grid {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .col-span-1, .col-span-2, .col-span-3, .col-span-4, .col-span-5, .col-span-6, 
  .col-span-7, .col-span-8, .col-span-9, .col-span-10, .col-span-11, .col-span-12 {
    width: 100%;
    margin-bottom: 0;
  }
  .column-bordered {
    border-right: none !important;
    border-bottom: 1px solid var(--rule);
    padding-right: 0 !important;
    padding-bottom: 20px;
    margin-bottom: 20px;
    padding-left: 0 !important;
  }
  .column-bordered:last-child {
    border-bottom: none;
    padding-bottom: 0;
    margin-bottom: 0;
  }
  
  /* Reset padding-left on mobile for columns that were offset */
  .col-span-6 {
    padding-left: 0 !important;
  }
  .col-span-4 {
    padding-left: 0 !important;
  }
  
  .display-xl {
    font-size: clamp(40px, 12vw, 60px);
  }
  
  .display-lg {
    font-size: clamp(32px, 8vw, 46px);
  }
}
"""

with open('css/styles.css', 'a') as f:
    f.write(css_append)

<?php
/**
 * @Entity @Table(name="drops")
 **/
class Drop
{
    /** @Id @Column(type="integer") @GeneratedValue **/
    protected $id;

    /** @Column(type="datetime") **/
    protected $dateAndTime;

    /** @Column(type="string") **/
    protected $timezone;

    /**
     * @OneToOne(targetEntity="Location")
     * @JoinColumn(name="location_id", referencedColumnName="id")
     */
    protected $location;

    /**
     * @var bool
     */
    private $localized = false;

    public function __construct( \DateTime $dateAndTime )
    {
        $this->localized = true;
        $this->setDateAndTime( $dateAndTime );
    }

    public function getId()
    {
        return $this->id;
    }

    public function getDateAndTime()
    {
        if ( !$this->localized ) {
            $this->dateAndTime->setTimeZone( new \DateTimeZone( $this->timezone ) );
        }
        return $this->dateAndTime;
    }

    public function setDateAndTime( \DateTime $dateAndTime )
    {
        $this->dateAndTime = $dateAndTime;
        $this->timezone = $dateAndTime->getTimeZone()->getName();
    }

    public function getLocation()
    {
        return $this->location;
    }

    public function setLocation( $location )
    {
        $this->location = $location;
    }
}
